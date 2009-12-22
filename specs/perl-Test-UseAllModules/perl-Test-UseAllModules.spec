# $Id$
# Authority: cmr
# Upstream: Kenichi Ishigaki <ishigaki$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-UseAllModules

Summary: do use_ok() for all the MANIFESTed modules
Name: perl-Test-UseAllModules
Version: 0.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-UseAllModules/

Source: http://www.cpan.org/authors/id/I/IS/ISHIGAKI/Test-UseAllModules-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::Manifest)
BuildRequires: perl(Test::More)
Requires: perl(Exporter)
Requires: perl(ExtUtils::Manifest)
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup


%description
do use_ok() for all the MANIFESTed modules.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Test::UseAllModules.3pm*
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/UseAllModules/
%{perl_vendorlib}/Test/UseAllModules.pm

%changelog
* Tue Dec 22 2009 Christoph Maser <cmr@financial.com> - 0.12-1
- Initial package. (using DAR)
