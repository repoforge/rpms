# $Id$
# Authority: cmr
# Upstream: Gisle Aas <gisle$activestate,com>
# Tag: test

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name libwww-perl

Summary: The World-Wide Web library for Perl
Name: perl-libwww-perl
Version: 5.826
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/libwww-perl/

Source: http://www.cpan.org/authors/id/G/GA/GAAS/libwww-perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.006
Requires: perl >= 0:5.006

%description
The World-Wide Web library for Perl.

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
%doc AUTHORS Changes MANIFEST META.yml README README.SSL
%doc %{_mandir}/man3/Bundle::LWP.3pm*
%{_bindir}/lwp-download
%{_bindir}/lwp-mirror
%{_bindir}/lwp-request
%{_bindir}/lwp-rget
%{perl_vendorlib}/Bundle/LWP.pm
%{perl_vendorlib}/File/Listing.pm
%{perl_vendorlib}/HTML/
%{perl_vendorlib}/HTTP/
%{perl_vendorlib}/LWP.pm
%{perl_vendorlib}/LWP/
%{perl_vendorlib}/Net/HTTP.pm
%{perl_vendorlib}/Net/HTTP/
%{perl_vendorlib}/Net/HTTPS.pm
%{perl_vendorlib}/WWW/RobotRules.pm
%{perl_vendorlib}/WWW/RobotRules/AnyDBM_File.pm
%{perl_vendorlib}/lwpcook.pod
%{perl_vendorlib}/lwptut.pod
%{_mandir}/man1/lwp-download.1.gz
%{_mandir}/man1/lwp-mirror.1.gz
%{_mandir}/man1/lwp-request.1.gz
%{_mandir}/man1/lwp-rget.1.gz
%{_mandir}/man3/File::Listing.3pm.gz
%{_mandir}/man3/HTML::*.3pm.gz
%{_mandir}/man3/HTTP::*.3pm.gz
%{_mandir}/man3/LWP.3pm.gz
%{_mandir}/man3/LWP::*.3pm.gz
%{_mandir}/man3/Net::HTTP.3pm.gz
%{_mandir}/man3/Net::HTTP::NB.3pm.gz
%{_mandir}/man3/WWW::RobotRules.3pm.gz
%{_mandir}/man3/WWW::RobotRules::AnyDBM_File.3pm.gz
%{_mandir}/man3/lwpcook.3pm.gz
%{_mandir}/man3/lwptut.3pm.gz


%changelog
* Thu Jul 23 2009 Christoph Maser <cmr@financial.com> - 5.826-1
- Initial package. (using DAR)
