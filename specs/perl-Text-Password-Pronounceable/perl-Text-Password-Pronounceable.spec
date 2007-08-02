# $Id$
# Authority: dries
# Upstream: Chia-liang Kao (&#39640;&#22025;&#33391;) <clkao$clkao,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Password-Pronounceable

Summary: Generate pronounceable passwords
Name: perl-Text-Password-Pronounceable
Version: 0.28
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Password-Pronounceable/

Source: http://search.cpan.org//CPAN/authors/id/C/CL/CLKAO/Text-Password-Pronounceable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Generate pronounceable passwords.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc %{_mandir}/man3/Text::Password::Pronounceable*
%{perl_vendorlib}/Text/Password/Pronounceable.pm
%dir %{perl_vendorlib}/Text/Password/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.28-1
- Initial package.
