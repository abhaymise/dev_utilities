1. Transfer Learning only
    1. Load a pretrained model
    2. Freeze all layer
    3. Extract features from FC layers
    4. Attach Linear FC head with num_classes as final output
    5. Initialise weights randomly
    6. Train with a higher LR for few epochs
    7. Evaluate
2. Fine Tuning
    1. Complete Experiment 1
    2. Make every layer trainable i.e unfreeze all layer
    3. Train with a lower LR for few epochs
    4. Evaluate
3. Custom Net
    1. Design custom small CNN
    2. Add nonlinearity to learn from high dimensional data
    3. Train
4. Multi resolution
    1. Augment data with multiple resolutions
        - Types of aug
            1. Zoom out and crop
            2. center cro
            3. resize to bigger res
    2. Train with all res
    3. Test time multi resolution inference
5. Parallel multi res inference for avg confidence preds
    1. Make pred on low res
    2. if pred_conf is high no action
    3. if pred_conf is very low no action
    4. if pred_conf is in some avg range [between low and high]
        1. take a higher resolution of the image
        2. make pred
        3. if conf is high make positive pred else make negative pred