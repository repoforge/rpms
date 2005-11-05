# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Archive-Tar

Summary: Archive-Tar module for perl
Name: perl-Archive-Tar
Version: 1.26
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Archive-Tar/

Source: http://www.cpan.org/modules/by-module/Archive/Archive-Tar-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503


%description
Module for manipulations of tar archives.


%prep
%setup -n %{real_name}-%{version} 


%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/*


%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.26-1
- Updated to release 1.26.

* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 1.08-0
- Initial package. (using DAR)
