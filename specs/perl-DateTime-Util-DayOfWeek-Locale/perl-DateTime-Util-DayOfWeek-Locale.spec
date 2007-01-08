# $Id$
# Authority: dries
# Upstream: MATSUNO&#9733;Tokuhiro <tokuhirom+cpan$gmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Util-DayOfWeek-Locale

Summary: DateTime Localized Day of Week
Name: perl-DateTime-Util-DayOfWeek-Locale
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Util-DayOfWeek-Locale/

Source: http://search.cpan.org//CPAN/authors/id/T/TO/TOKUHIROM/DateTime-Util-DayOfWeek-Locale-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
DateTime Localized Day of Week Utilities.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/DateTime::Util::DayOfWeek::Locale*
%{perl_vendorlib}/DateTime/Util/DayOfWeek/Locale.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
