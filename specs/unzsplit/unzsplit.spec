# $Id$
# Authority: dag
# Upstream: Jurij Ivastsuk-Kienbaum

Summary: Glue, decompress and restore zsplit images
Name: unzsplit
Version: 1.0.1
Release: 1
License: GPL
Group: System Environment/Base
URL: http://www.device-image.de/

Source: http://www.device-image.de/download/unzsplit_src-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel

%description
zunsplit decompresses, glues and restores zsplit images to its original form.

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
%doc %{_mandir}/man8/unzsplit.8*
%{_bindir}/unzsplit

%changelog
* Sun May 22 2005 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Initial package. (using DAR)
