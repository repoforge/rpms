# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-Title

Summary: Perl module to get the titles of things on the web in a sensible way
Name: perl-URI-Title
Version: 1.82
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-Title/

Source: http://www.cpan.org/modules/by-module/URI/URI-Title-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-URI-Title is a Perl module to get the titles of things on the web
in a sensible way.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/URI::Title.3pm*
#%doc %{_mandir}/man3/URI::Title::*.3pm*
%dir %{perl_vendorlib}/URI/
%{perl_vendorlib}/URI/Title/
%{perl_vendorlib}/URI/title.pl
%{perl_vendorlib}/URI/Title.pm

%changelog
* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 1.82-1
- Updated to version 1.82.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.70-1
- Updated to release 1.70.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.62-1
- Initial package. (using DAR)
