# $Id$
# Authority: dag
# Upstream: Brian Cassidy <bricas$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-Template

Summary: Object for handling URI templates
Name: perl-URI-Template
Version: 0.13
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-Template/

Source: http://www.cpan.org/modules/by-module/URI/URI-Template-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.6.0


%description
perl-URI-Template is a Perl module that provides an object
for handling URI templates.

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
%doc %{_mandir}/man3/URI::Template.3pm*
%dir %{perl_vendorlib}/URI/
#%{perl_vendorlib}/URI/Template/
%{perl_vendorlib}/URI/Template.pm

%changelog
* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 0.13-1
- Updated to release 0.13.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
