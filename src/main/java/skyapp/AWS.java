package skyapp;

import java.io.File;

import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.GetObjectRequest;
import com.amazonaws.services.s3.model.PutObjectRequest;

public class AWS {
    final AmazonS3 s3 = AmazonS3ClientBuilder.defaultClient();

    public void downloadFile(String bucketName, String storageKey, File localFile) {
        GetObjectRequest request = new GetObjectRequest(bucketName, storageKey);
        s3.getObject(request, localFile);
    }

    public void uploadFile(String bucketName, String localFile, String storageKey) {
        PutObjectRequest request = new PutObjectRequest(bucketName, storageKey, localFile);
        s3.putObject(request);
    }
}
