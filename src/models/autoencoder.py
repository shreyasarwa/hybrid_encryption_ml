from tensorflow.keras import Model
from src.models.encoder import build_encoder
from src.models.decoder import build_decoder

class HybridAutoencoder:
    @staticmethod
    def build(input_shape):
        encoder = build_encoder(input_shape)
        decoder = build_decoder(encoder.output_shape[1:])
        
        autoencoder_input = encoder.input
        autoencoder_output = decoder(encoder.output)
        
        model = Model(autoencoder_input, autoencoder_output, name="CNN_Autoencoder")
        return model, encoder, decoder