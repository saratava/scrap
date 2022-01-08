function transform(line) {
    var values = line.split('|');
    var obj = new Object();
    obj.content = values[0];
    obj.score = values[1];
    obj.thumbsUpCount = values[2];
    obj.reviewCreatedVersion = values[3];
    obj.at = values[4];
    obj.replyContent = values[5];
    var jsonString = JSON.stringify(obj);
    return jsonString;
}