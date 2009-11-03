# $Id$
# Authority: dag
# Upstream: Jurij Ivastsuk-Kienbaum

Summary: Split, compress and backup devices and files to zsplit images
Name: zsplit
Version: 1.2.0
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.device-image.de/

Source: http://www.device-image.de/download/zsplit_src-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel, gcc-c++

%description
zsplit splits, compresses and backups devices and files to zsplit images.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL NEWS README TODO
%doc %{_mandir}/man8/zsplit.8*
%{_bindir}/zsplit

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.0-1.2
- Rebuild for Fedora Core 5.

* Sat Jun 18 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.0-1
- Updated to release 1.2.0.

* Sun May 22 2005 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Initial package. (using DAR)
