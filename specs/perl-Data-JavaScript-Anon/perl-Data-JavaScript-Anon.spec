# $Id$
# Authority: dag
# Upstream: Adam Kennedy <adamk$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-JavaScript-Anon

Summary: Dump big dumb Perl structs to anonymous JavaScript structs
Name: perl-Data-JavaScript-Anon
Version: 1.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-JavaScript-Anon/

Source: http://www.cpan.org/modules/by-module/Data/Data-JavaScript-Anon-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(File::Spec) >= 0.82
BuildRequires: perl(Test::More) >= 0.47
Requires: perl >= 0:5.005

%description
Dump big dumb Perl structs to anonymous JavaScript structs.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Data::JavaScript::Anon.3pm*
%dir %{perl_vendorlib}/Data/
%dir %{perl_vendorlib}/Data/JavaScript/
#%{perl_vendorlib}/Data/JavaScript/Anon/
%{perl_vendorlib}/Data/JavaScript/Anon.pm

%changelog
* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 1.03-1
- Updated to version 1.03.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 1.01-1
- Updated to release 1.01.

* Sat Mar 08 2008 Dag Wieers <dag@wieers.com> - 0.9-1
- Initial package. (using DAR)
