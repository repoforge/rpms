# $Id$
# Authority: dag
# Upstream: Tim Jenness <t,jenness$jach,hawaii,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Temp

Summary: Perl module that returns name and handle of a temporary file safely
Name: perl-File-Temp
Version: 0.18
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Temp/

Source: http://www.cpan.org/modules/by-module/File/File-Temp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-File-Temp is a Perl module that returns name and handle
of a temporary file safely.

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
* Mon Aug 06 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Initial package. (using DAR)
