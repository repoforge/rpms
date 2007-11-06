# $Id$
# Authority: dries
# Upstream: Derek Price <derek$ximbiot,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Wiki-Toolkit-Formatter-Mediawiki

Summary: Mediawiki-style formatter for Wiki::Toolkit
Name: perl-Wiki-Toolkit-Formatter-Mediawiki
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Wiki-Toolkit-Formatter-Mediawiki/

Source: http://search.cpan.org//CPAN/authors/id/D/DP/DPRICE/Wiki-Toolkit-Formatter-Mediawiki-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
A Mediawiki-style formatter for Wiki::Toolkit.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Wiki::Toolkit::Formatter::Mediawiki*
%dir %{perl_vendorlib}/Wiki/Toolkit/
%dir %{perl_vendorlib}/Wiki/Toolkit/Formatter/
%{perl_vendorlib}/Wiki/Toolkit/Formatter/Mediawiki.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
