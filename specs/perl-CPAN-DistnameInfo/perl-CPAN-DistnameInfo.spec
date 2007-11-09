# $Id$
# Authority: dries
# Upstream: Graham Barr <gbarr$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CPAN-DistnameInfo

Summary: Extract distribution name and version from a distribution filename
Name: perl-CPAN-DistnameInfo
Version: 0.06
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CPAN-DistnameInfo/

Source: http://www.cpan.org/modules/by-module/CPAN/CPAN-DistnameInfo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Many online services that are centered around CPAN attempt to associate
multiple uploads by extracting a distribution name from the filename of
the upload. For most distributions this is easy as they have used
ExtUtils::MakeMaker or Module::Build to create the distribution, which
results in a uniform name. But sadly not all uploads are created in this
way.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/CPAN/
%{perl_vendorlib}/CPAN/DistnameInfo.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1.2
- Rebuild for Fedora Core 5.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
