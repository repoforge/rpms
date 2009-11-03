# $Id$
# Authority: dries
# Upstream: Chia-liang Kao <clkao$clkao,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Finance-TW-TSEQuote

Summary: Check stock quotes from Taiwan Security Exchange
Name: perl-Finance-TW-TSEQuote
Version: 0.27
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Finance-TW-TSEQuote/

Source: http://www.cpan.org/modules/by-module/Finance/Finance-TW-TSEQuote-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Check stock quotes from Taiwan Security Exchange.

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
%doc CHANGES MANIFEST META.yml
%doc %{_mandir}/man1/pfq.1*
%doc %{_mandir}/man3/Finance::TW::TSEQuote.3pm*
%{_bindir}/pfq
%dir %{perl_vendorlib}/Finance/
%dir %{perl_vendorlib}/Finance/TW/
#%{perl_vendorlib}/Finance/TW/TSEQuote/
%{perl_vendorlib}/Finance/TW/TSEQuote.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.27-1
- Updated to release 0.27.

* Thu Jan 04 2007 Dries Verachtert <dries@ulyssis.org> - 0.26-1
- Updated to release 0.26.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Initial package.
