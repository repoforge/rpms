# $Id$
# Authority: dries
# Upstream: Norman Walsh <ndw$nwalsh,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DelimMatch
%define real_version 1.06

Summary: Find regexp delimited strings with proper nesting
Name: perl-DelimMatch
Version: 1.06a
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DelimMatch/

Source: http://www.cpan.org/authors/id/N/NW/NWALSH/DelimMatch-%{version}a.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
DelimMatch allows you to match delimited substrings in a buffer.
The delimiters can be specified with any regular expression and
the start and end delimiters need not be the same.  If the
delimited text is properly nested, entire nested groups are
returned.

%prep
%setup -n %{real_name}-%{real_version}

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/DelimMatch.pm
%{perl_vendorlib}/auto/Text/DelimMatch

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.06a-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.06a-1
- Initial package.
