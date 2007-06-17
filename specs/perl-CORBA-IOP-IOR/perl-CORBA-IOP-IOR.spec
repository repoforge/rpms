# $Id$
# Authority: dries
# Upstream: Philip Aston <philipa$parallax,co,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name CORBA-IOP-IOR

Summary: Decode, munge, and re-encode CORBA IORs
Name: perl-CORBA-IOP-IOR
Version: 0.1
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CORBA-IOP-IOR/

Source: http://search.cpan.org/CPAN/authors/id/P/PH/PHILIPA/CORBA-IOP-IOR-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
CORBA::IOP::IOR is a handy module for processing IORs. I've found
it very useful for debugging CORBA interoperability.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
#%doc %{_mandir}/man3/*
%{perl_vendorlib}/CORBA/IOP

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.1-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.1-1
- Initial package.
