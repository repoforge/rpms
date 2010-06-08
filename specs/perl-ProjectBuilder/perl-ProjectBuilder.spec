# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ProjectBuilder

Summary: Perl module providing multi-OSes (Linux/Solaris/...) Continuous Packaging
Name: perl-ProjectBuilder
Version: 0.9.10
Release: 1%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://trac.project-builder.org/

Source: ftp://ftp.project-builder.org/src/ProjectBuilder-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: perl >= 5.8.4

%description
ProjectBuilder is a perl module providing set of functions
to help develop packages for projects and deal
with different Operating systems (Linux distributions, Solaris, ...).
It implements a Continuous Packaging approach.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}" CONFDIR="%{_sysconfdir}/pb" MANDIR="%{_mandir}"
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;
find %{buildroot} -name perllocal.pod -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL NEWS README
%doc %{_mandir}/man1/pbdistrocheck.1*
%doc %{_mandir}/man3/ProjectBuilder::*.3pm*
%doc %{_mandir}/man5/pb.conf.5*
%config(noreplace) %{_sysconfdir}/pb/
%{perl_vendorlib}/ProjectBuilder/
%{_bindir}/pbdistrocheck

%changelog
* Tue Jun 08 2010 Dag Wieers <dag@wieers.com> - 0.9.10-1
- Initial package. (using DAR)
