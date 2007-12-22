# $Id$
# Authority: dag
# Upstream: Per Einar Ellefsen <pereinar$oslo,online,no>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Which

Summary: Portable implementation of the 'which' utility
Name: perl-File-Which
Version: 0.05
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Which/

Source: http://www.cpan.org/modules/by-module/File/File-Which-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

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
* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
