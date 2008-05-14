# $Id$
# Authority: dag
# Upstream: Hans Dieter Pearcey <hdp$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Perl-Version

Summary: Parse and manipulate Perl version strings
Name: perl-Perl-Version
Version: 1.007
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Perl-Version/

Source: http://www.cpan.org/modules/by-module/Perl/Perl-Version-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Parse and manipulate Perl version strings.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml Notes.txt README SIGNATURE examples/
%doc %{_mandir}/man3/Perl::Version.3pm*
%dir %{perl_vendorlib}/Perl/
#%{perl_vendorlib}/Perl/Version/
%{perl_vendorlib}/Perl/Version.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.007-1
- Updated to release 1.007.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.004-1
- Updated to release 1.004.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.002-1
- Initial package. (using DAR)
