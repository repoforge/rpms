# $Id$
# Authority: dag

Summary: Utility to convert an Alcohol 120% image to the standard ISO-9660 format
Name: mdf2iso
Version: 0.3.0
Release: 1
License: GPL
Group: Applications/File
URL: http://mdf2iso.berlios.de/

Source: http://download.berlios.de/mdf2iso/mdf2iso-%{version}-src.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
mdf2iso is a very simple utility to convert an Alcohol 120% bin
image to the standard ISO-9660 format.

%prep
%setup -n %{name}

%{__chmod} 0644 ChangeLog *.txt

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
%doc ChangeLog *.txt
%{_bindir}/mdf2iso

%changelog
* Wed Nov 05 2008 Dag Wieers <dag@wieers.com> - 0.3.0-1
- Initial package. (using DAR)
