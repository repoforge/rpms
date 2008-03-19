# $Id$
# Authority: dag

Summary: xml2swf and swf2xml processor
Name: swfmill
Version: 0.2.12
Release: 1
License: GPL
Group: Applications/File
URL: http://swfmill.org/

Source: http://swfmill.org/releases/swfmill-%{version}.tar.gz
#Source: http://swfmill.org/pre/swfmill-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: freetype-devel >= 2.0
BuildRequires: libpng-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: zlib-devel

%description
swfmill is an xml2swf and swf2xml processor with import
functionalities.

It's most common use is the generation of asset libraries
containing images (PNG and JPEG), fonts (TTF) or other SWF
movies for use with MTASC- or haXe-compiled ActionScript,
although swfmill can be used to produce both simple and complex
SWF structures.

* built around an XSLT/EXSLT processor (libxslt)
* input and output of the XSLT transformation can be either XML
  or binary SWF
* XSLT commands for importing PNG, JPEG, TTF and SWF, and for
  mapping SWF ID numbers
* built-in "simple dialect" to support library creation and
  building simple SWFs

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL NEWS README TODO
%{_bindir}/swfmill
%{_libdir}/libswfmillxslt.so.*
%{_libdir}/libswft.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/libswfmillxslt.so
%{_libdir}/libswft.so
%exclude %{_libdir}/libswfmillxslt.la
%exclude %{_libdir}/libswft.la

%changelog
* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 0.2.12-1
- Initial package. (using DAR)
