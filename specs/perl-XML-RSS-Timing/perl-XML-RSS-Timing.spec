# $Id$

# Authority: dries
# Upstream: Sean M. Burke <sburke$cpan,org>

%define real_name XML-RSS-Timing
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Support for RSS skipHours, skipDays and sy:update
Name: perl-XML-RSS-Timing
Version: 1.07
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-RSS-Timing/

Source: http://www.cpan.org/modules/by-module/XML/XML-RSS-Timing-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
RSS/RDF modules can use the skipHours, skipDays, ttl, and sy:update*
elements to express what days/times they won't update, so that RSS/RDF
clients can conserve network resources by not bothering to poll a feed
more than once during such a period.

This Perl module is for taking in the RSS/RDF skipHours, skipDays, ttl,
and sy:update* elements' values, and figuring out when they say new
content might be available.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML/RSS/Timing.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.07-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Initial package.
