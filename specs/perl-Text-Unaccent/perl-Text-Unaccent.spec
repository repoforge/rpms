# $Id$
# Authority: dries
# Upstream: Loic Dachary <loic$senga,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Unaccent

Summary: Remove accents from a string
Name: perl-Text-Unaccent
Version: 1.08
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Unaccent/

Source: http://search.cpan.org/CPAN/authors/id/L/LD/LDACHARY/Text-Unaccent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Text::Unaccent is a module that provides functions to remove accents
from a string.  For instance the string été will become ete.  The
charset of the input string is specified as an argument. The input is
converted to UTF-16 using iconv(3), accents are stripped and the
result is converted back to the original charset. The iconv -l
command on GNU/Linux will show all charset supported.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Text/Unaccent.pm
%{perl_vendorarch}/auto/Text/Unaccent

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.08-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Initial package.
