/***************************************************************************
  qgsmaplayerfactory.cpp
  --------------------------------------
  Date                 : March 2021
  Copyright            : (C) 2021 by Nyall Dawson
  Email                : nyall dot dawson at gmail dot com
***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

#include "qgsmaplayerfactory.h"
#include "qgsvectorlayer.h"
#include "qgsrasterlayer.h"
#include "qgsmeshlayer.h"
#include "qgspointcloudlayer.h"
#include "qgsvectortilelayer.h"
#include "qgsannotationlayer.h"

QgsMapLayerType QgsMapLayerFactory::typeFromString( const QString &string, bool &ok )
{
  ok = true;
  if ( string.compare( QLatin1String( "vector" ), Qt::CaseInsensitive ) == 0 )
    return QgsMapLayerType::VectorLayer;
  else if ( string.compare( QLatin1String( "raster" ), Qt::CaseInsensitive ) == 0 )
    return QgsMapLayerType::RasterLayer;
  else if ( string.compare( QLatin1String( "mesh" ), Qt::CaseInsensitive ) == 0 )
    return QgsMapLayerType::MeshLayer;
  else if ( string.compare( QLatin1String( "vector-tile" ), Qt::CaseInsensitive ) == 0 )
    return QgsMapLayerType::VectorTileLayer;
  else if ( string.compare( QLatin1String( "point-cloud" ), Qt::CaseInsensitive ) == 0 )
    return QgsMapLayerType::PointCloudLayer;
  else if ( string.compare( QLatin1String( "plugin" ), Qt::CaseInsensitive ) == 0 )
    return QgsMapLayerType::PluginLayer;
  else if ( string.compare( QLatin1String( "annotation" ), Qt::CaseInsensitive ) == 0 )
    return QgsMapLayerType::AnnotationLayer;

  ok = false;
  return QgsMapLayerType::VectorLayer;
}

QString QgsMapLayerFactory::typeToString( QgsMapLayerType type )
{
  switch ( type )
  {
    case QgsMapLayerType::VectorLayer:
      return QStringLiteral( "vector" );
    case QgsMapLayerType::RasterLayer:
      return QStringLiteral( "raster" );
    case QgsMapLayerType::PluginLayer:
      return QStringLiteral( "plugin" );
    case QgsMapLayerType::MeshLayer:
      return QStringLiteral( "mesh" );
    case QgsMapLayerType::VectorTileLayer:
      return QStringLiteral( "vector-tile" );
    case QgsMapLayerType::AnnotationLayer:
      return QStringLiteral( "annotation" );
    case QgsMapLayerType::PointCloudLayer:
      return QStringLiteral( "point-cloud" );
  }
  return QString();
}

QgsMapLayer *QgsMapLayerFactory::createLayer( const QString &uri, const QString &name, QgsMapLayerType type, const QString &provider, const QgsCoordinateTransformContext &transformContext )
{
  switch ( type )
  {
    case QgsMapLayerType::VectorLayer:
    {
      QgsVectorLayer::LayerOptions options;
      options.transformContext = transformContext;
      return new QgsVectorLayer( uri, name, provider, options );
    }

    case QgsMapLayerType::RasterLayer:
    {
      QgsRasterLayer::LayerOptions options;
      options.transformContext = transformContext;
      return new QgsRasterLayer( uri, name, provider, options );
    }

    case QgsMapLayerType::MeshLayer:
    {
      QgsMeshLayer::LayerOptions options;
      options.transformContext = transformContext;
      return new QgsMeshLayer( uri, name, provider, options );
    }

    case QgsMapLayerType::VectorTileLayer:
      return new QgsVectorTileLayer( uri, name );

    case QgsMapLayerType::AnnotationLayer:
      return new QgsAnnotationLayer( name, QgsAnnotationLayer::LayerOptions( transformContext ) );

    case QgsMapLayerType::PointCloudLayer:
    {
      QgsPointCloudLayer::LayerOptions options;
      options.transformContext = transformContext;
      return new QgsPointCloudLayer( uri, name, provider, options );
    }

    case QgsMapLayerType::PluginLayer:
      break;
  }
  return nullptr;
}
