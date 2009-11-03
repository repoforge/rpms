# $Id$
# Authority: dag
# Upstream: Paul Seamons <perl$seamons,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Ex

Summary: Perl module to make powerful application writing fun and easy
Name: perl-CGI-Ex
Version: 2.27
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Ex/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Ex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
BuildRequires: perl(Template::Alloy) >= 1.004


%description
perl-CGI-Ex is a Perl module to make powerful application writing fun and easy.

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

### Clean up docs
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README samples/
%doc %{_mandir}/man3/CGI::Ex.3pm*
%doc %{_mandir}/man3/CGI::Ex::*.3pm*
%dir %{perl_vendorlib}/CGI/
%{perl_vendorlib}/CGI/Ex/
%{perl_vendorlib}/CGI/Ex.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 2.27-1
- Updated to version 2.27.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 2.24-1
- Updated to release 2.24.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 2.23-1
- Updated to release 2.23.

* Wed Nov 07 2007 Dag Wieers <dag@wieers.com> - 2.21-1
- Updated to release 2.21.

* Fri Aug 03 2007 Dag Wieers <dag@wieers.com> - 2.18-1
- Initial package. (using DAR)
