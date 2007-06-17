# $Id$
# Authority: dries
# Upstream: &#2716;&#2738;&#2727;&#2736; &#2745;. &#2741;&#2765;&#2735;&#2750;&#2744; <jaldhar$braincells,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Calendar-Discordian

Summary: Extension for the Discordian Calendar
Name: perl-DateTime-Calendar-Discordian
Version: 0.9.4
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Calendar-Discordian/

Source: http://search.cpan.org//CPAN/authors/id/J/JA/JALDHAR/DateTime-Calendar-Discordian-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This is a module that implements the Discordian calendar made popular
in the "Illuminatus!" trilogy by Robert Shea and Robert Anton Wilson and
by the Church of the SubGenius.  It follows the DateTime API.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Calendar/
%{perl_vendorlib}/DateTime/Calendar/Discordian.pm

%changelog
* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.4-1
- Initial package.
