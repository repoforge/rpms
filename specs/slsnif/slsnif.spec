# $Id$
# Authority: dag

Summary: Serial line Sniffer
Name: slsnif
Version: 0.4.4
Release: 1
License: GPL
Group: Applications/Communications
URL: http://slsnif.sourceforge.net/

Source: http://dl.sf.net/sourceforge/slsnif/slsnif-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
slsnif is a serial port logging tool. slsnif listens to the specified serialx
port and logs all data going through this port in both directions.

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO slsnifrc-example
%doc %{_mandir}/man1/slsnif.1*
%{_bindir}/slsnif

%changelog
* Wed Mar 12 2008 Dag Wieers <dag@wieers.com> - 0.4.4-1
- Initial package. (using DAR)
