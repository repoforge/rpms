# $Id$
# Authority: dries
# Upstream: tujikawa$rednoah,com

Summary: Download utility with BitTorrent and Metalink support
Name: aria2
Version: 0.7.2
Release: 1
License: GPL
Group: Productivity/Networking
URL: http://aria2.sourceforge.net/

Source: http://dl.sf.net/aria2/aria2-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel, libxml2-devel, gcc-c++, gettext

%description
aria2 is a download utility with resuming and segmented downloading.
Supported protocols are HTTP/HTTPS/FTP/BitTorrent/Metalink.

%prep
%setup
 
%build
%configure --enable-metalink --disable-xmltest CPPFLAGS=-I/usr/include/libxml2
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang aria2c

#%clean
#%{__rm} -rf %{buildroot}
  
%files -f aria2c.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING NEWS README AUTHORS TODO
%{_bindir}/aria2c

%changelog
* Mon Aug 21 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.2-1
- Updated to 0.7.2.

* Tue Aug 15 2006 Dries Verachtert <dries@ulyssis.org>
- Updated to 0.7.1.

* Sat Aug 12 2006 Dries Verachtert <dries@ulyssis.org>
- Updated to 0.7.0.

* Fri Jul 28 2006 Anthony Bryan <anthonybryan@gmail.com>
- Update to version 0.6.0+1 and FC6
 
* Mon Jun 5 2006 Malcolm A Hussain-Gambles <malcolm@secpay7.force9.co.uk>
- First release of this package by me
