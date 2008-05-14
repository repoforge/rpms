# $Id$
# Authority: dag
# Upstream: Alexey Tourbin <at$altlinux,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name rpm-build-perl
%define real_version 0.006008

Summary: Calculate dependencies for Perl sources
Name: perl-rpm-build-perl
Version: 0.6.8
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/rpm-build-perl/

#Source: http://www.cpan.org/modules/by-module/B/rpm-build-perl-%{version}.tar.gz
Source: http://www.cpan.org/authors/id/A/AT/ATOURBIN/rpm-build-perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Calculate dependencies for Perl sources.

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
%doc Changes MANIFEST META.yml README README.ALT
%doc %{_mandir}/man1/perl.prov.1*
#%doc %{_mandir}/man1/perl.prov.files.1*
%doc %{_mandir}/man1/perl.req.1*
%doc %{_mandir}/man3/B::PerlReq.3pm*
%doc %{_mandir}/man3/PerlReq::Utils.3pm*
%{_bindir}/perl.prov
%{_bindir}/perl.prov.files
%{_bindir}/perl.req
%{_bindir}/perl.req.files
%dir %{perl_vendorlib}/B/
%{perl_vendorlib}/B/PerlReq.pm
%dir %{perl_vendorlib}/PerlReq/
%{perl_vendorlib}/PerlReq/Utils.pm
%{perl_vendorlib}/fake.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.6.8-1
- Updated to release 0.6.8.

* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 0.6.7-1
- Updated to release 0.6.7.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.6.6-1
- Updated to release 0.6.6.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.6.5-1
- Initial package. (using DAR)
