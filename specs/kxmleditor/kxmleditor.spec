# $Id: $

# Authority: dries
# Upstream: 

Summary: XML Editor
Name: kxmleditor
Version: 1.0.0
Release: 1
License: GPL
Group: Applications/Editors
URL: http://kxmleditor.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/kxmleditor/kxmleditor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, libpng-devel, libart_lgpl-devel, arts-devel, gcc-c++, gettext, XFree86-devel, zlib-devel, qt-devel, libjpeg-devel, kdelibs-devel, gift

# Screenshot: http://kxmleditor.sourceforge.net/screenshot.png
# ScreenshotURL: http://kxmleditor.sourceforge.net/screenshots.htm

%description
KXML Editor is program, that display and edit contents of XML file. Main
features: 
* Drag and drop editing, clipboard support 
* Use DOM level 2 Qt library parser 
* KParts technology support 
* DCOP technology support 
* Editing KOffice compressed files 

%prep
%setup

%build
%configure
sed -i "s/<UI version=\"3.2\" /<UI version=\"3.3\"/g;" $(find . | egrep "\.ui$")
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_bindir}/*
%{_libdir}/*.so.*

%changelog
* Sun May 30 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.0-1
- Initial package.
