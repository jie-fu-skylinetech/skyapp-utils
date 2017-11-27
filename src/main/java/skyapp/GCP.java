package skyapp;

import java.io.FileInputStream;
import java.nio.file.Path;

import com.google.cloud.storage.Blob;
import com.google.cloud.storage.BlobInfo;
import com.google.cloud.storage.Storage;
import com.google.cloud.storage.StorageOptions;

public class GCP {
    public void uploadFile(String bucketName, Path localFile, String storageKey) {
        Storage storage = StorageOptions.getDefaultInstance().getService();
        try {
            Blob blob = storage.create(BlobInfo.newBuilder(bucketName, storageKey).build(),
                    new FileInputStream(localFile.toFile()));
        } catch (Exception ex) {
            throw new Error(ex.getMessage());
        }
    }

    public void downloadFile(String bucketName, String storageKey, Path localFile) {
        Storage storage = StorageOptions.getDefaultInstance().getService();
        storage.create(BlobInfo.newBuilder(bucketName, storageKey).build()).downloadTo(localFile);
    }
}