# $Id$
# Authority: dag

%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)

Summary: Tool similar to debootstrap for RPM based distributions
Name: rpmbootstrap
Version: 0.9.10
Release: 1.%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://trac.project-builder.org/

Source: ftp://ftp.project-builder.org/src/rpmbootstrap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: perl >= 5.8.4
Requires: perl-libwww-perl
Requires: perl-ProjectBuilder

%description
rpmbootstrap is a tool similar to debootstrap for RPM based distributions.
It helps building a chrooted environment for the related distribution

%prep
%setup

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL NEWS README
%doc %{_mandir}/man1/rpmbootstrap.1*
%{_bindir}/rpmbootstrap

%changelog
* Tue Jun 08 2010 Dag Wieers <dag@wieers.com> - 0.9.10-1
- Initial package. (using DAR)
