package skyapp;

import java.nio.file.Files;
import java.nio.file.Path;

import com.google.cloud.storage.BlobInfo;
import com.google.cloud.storage.Storage;
import com.google.cloud.storage.StorageOptions;

public class GCP {
    public void uploadFile(String bucketName, Path localFile, String storageKey) {
        byte[] content = null;
        try {
            content = Files.readAllBytes(localFile);
        } catch (Exception ex) {
            throw new Error(ex.getMessage(), ex);
        } finally {
            BlobInfo bi = BlobInfo.newBuilder(bucketName, storageKey).build();
            Storage storage = StorageOptions.getDefaultInstance().getService();
            storage.create(bi, content);
        }
    }

    public void downloadFile(String bucketName, String storageKey, Path localFile) {
        Storage storage = StorageOptions.getDefaultInstance().getService();
        storage.create(BlobInfo.newBuilder(bucketName, storageKey).build()).downloadTo(localFile);
    }
}