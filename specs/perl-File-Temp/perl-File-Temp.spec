# $Id$
# Authority: dag
# Upstream: Tim Jenness <tjenness$cpan,org>
# RFX: el3 el4 el5

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Temp

Summary: Return name and handle of a temporary file safely
Name: perl-File-Temp
Version: 0.22
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Temp/

Source: http://search.cpan.org/CPAN/authors/id/T/TJ/TJENNESS/File-Temp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Return name and handle of a temporary file safely.

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
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/File::Temp.3pm*
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/Temp.pm

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.22-1
- Updated to version 0.22.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.20-1
- Updated to release 0.20.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.19-1
- Updated to release 0.19.

* Mon Aug 06 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Initial package. (using DAR)
