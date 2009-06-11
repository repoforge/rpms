# $Id$
# Authority: dries
# Upstream: &#33673;&#27931; <kenwu$mail,tnssh,tn,edu,tw>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Shorten-KUSO

Summary: Shorten urls with KUSO
Name: perl-WWW-Shorten-KUSO
Version: 0.3
Release: 1.3
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Shorten-KUSO/

Source: http://search.cpan.org/CPAN/authors/id/K/KE/KENWU/WWW-Shorten-KUSO-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl(WWW::Shorten)

%description
Shorten URL using http://KUSO.CC/ .

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
%doc %{_mandir}/man3/*
%{perl_vendorlib}/WWW/Shorten/KUSO.pm

%changelog
* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 0.3-1.3
- Add dependency for perl(WWW::Shorten)

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1.2
- Rebuild for Fedora Core 5.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
