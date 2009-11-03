# $Id$
# Authority: dag
# Upstream: Per Einar Ellefsen <pereinar$oslo,online,no>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Which

Summary: Portable implementation of the 'which' utility
Name: perl-File-Which
Version: 1.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Which/

Source: http://www.cpan.org/modules/by-module/File/File-Which-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# From yaml build_requires
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Spec) >= 0.60
BuildRequires: perl(Getopt::Std)
#BuildRequires: perl(Test::More) >= 0.80  <- kills el4 build

%description
Portable implementation of the `which' utility.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man1/pwhich.1*
%doc %{_mandir}/man3/File::Which.3pm*
%{_bindir}/pwhich
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/Which.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 1.07-1
- Updated to version 1.07.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
