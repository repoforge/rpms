# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name TimeDate

Summary: TimeDate module for perl
Name: perl-TimeDate
Version: 1.16
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/TimeDate/

Source: http://search.cpan.org/CPAN/authors/id/G/GB/GBARR/TimeDate-%{version}.tar.gz
#Source: http://www.cpan.org/modules/by-module/TimeDate/TimeDate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
TimeDate module for perl

%prep
%setup -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL \
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
%doc ChangeLog MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Date/
%{perl_vendorlib}/Time/

%changelog
* Mon Feb 21 2005 Dag Wieers <dag@wieers.com> - 1.16-1
- Cosmetic cleanup.

* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 1.16-0
- Initial package. (using DAR)
