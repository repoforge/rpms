# $Id$

# Authority: dries
# Upstream: T.J. Mather <tjmather$maxmind,com>

%define real_name XML-RegExp
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Regular expressions for XML tokens
Name: perl-XML-RegExp
Version: 0.03
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-RegExp/

Source: http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/XML-RegExp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This package contains regular expressions for the following XML tokens:
BaseChar, Ideographic, Letter, Digit, Extender, CombiningChar, NameChar,
EntityRef, CharRef, Reference, Name, NmToken, and AttValue.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML/RegExp.pm

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
