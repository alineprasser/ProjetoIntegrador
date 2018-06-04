#if 1
#include <SPI.h>
#include <PN532_SPI.h>
#include <PN532.h>
#include <NfcAdapter.h>

PN532_SPI pn532spi(SPI, 10);
NfcAdapter nfc = NfcAdapter(pn532spi);
#else 0 

#include <Wire.h>
#include <PN532_I2C.h>
#include <PN532.h>
#include <NfcAdapter.h>

PN532_I2C pn532_i2c(Wire);
NfcAdapter nfc = NfcAdapter(pn532_i2c);
#endif

void setup(void) {
  Serial.begin(9600);
  //Serial.println("Leitor NFC!");
  nfc.begin();
  //Serial.println("Aproxime uma tag NFC ao leitor.");
}

void loop(void) {
  

  if (nfc.tagPresent())
  {
    NfcTag tag = nfc.read();
    //Serial.println(tag.getTagType());
    //Serial.print("UID: ");
    Serial.println(tag.getUidString());
    /*
    if (tag.hasNdefMessage()) // caso a tag tenha uma mensagem gravada
    {

      NdefMessage message = tag.getNdefMessage();
      Serial.print("\nMensagem desta tag: ");
      Serial.print(message.getRecordCount());
      Serial.print(" Mensagem");
      if (message.getRecordCount() != 1) {
        Serial.print("(s)");
      }
      Serial.println(".");

      // loop entre as mensagens, imprimindo cada uma delas
      int recordCount = message.getRecordCount();
      for (int i = 0; i < recordCount; i++)
      {
        Serial.print("\nMensagem gravada na tag: ");Serial.println(i+1);
        NdefRecord record = message.getRecord(i);

        Serial.print("  TNF: ");Serial.println(record.getTnf());
        Serial.print("  Tipo: ");Serial.println(record.getType()); // será "" para TNF_EMPTY

        int payloadLength = record.getPayloadLength();
        byte payload[payloadLength];
        record.getPayload(payload);

        // Print the Hex and Printable Characters
        Serial.print("  Mensagem (HEX): ");
        PrintHexChar(payload, payloadLength);

        // Force the data into a String (might work depending on the content)
        // Real code should use smarter processing
        String payloadAsString = "";
        for (int c = 0; c < payloadLength; c++) {
          payloadAsString += (char)payload[c];
          //Serial.write(payload);
        }
        Serial.print("  Mensagem gravada: ");
        Serial.println(payloadAsString);
        //Serial.write(payloadAsString); //envia pro pc a mensagem gravada

        // id is probably blank and will return ""
        String uid = record.getId();
        if (uid != "") {
          Serial.print("  ID: ");Serial.println(uid);
        }
      }
    }*/
  }
  delay(800);
}
