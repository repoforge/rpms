# $Id$
# Authority: dag
# Upstream: Jaap Karssenberg <pardus$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-MimeInfo

Summary: Perl module to determine file type
Name: perl-File-MimeInfo
Version: 0.14
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-MimeInfo/

Source: http://www.cpan.org/modules/by-module/File/File-MimeInfo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker), perl(Module::Build)
Requires: perl

%description
File-MimeInfo is a Perl module to determine file type.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man1/mimeopen.1*
%doc %{_mandir}/man1/mimetype.1*
%doc %{_mandir}/man3/File::MimeInfo.3pm*
%doc %{_mandir}/man3/File::MimeInfo::*.3pm*
%{_bindir}/mimeopen
%{_bindir}/mimetype
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/MimeInfo/
%{perl_vendorlib}/File/MimeInfo.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.14-1
- Updated to release 0.14.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.13-1
- Initial package. (using DAR)
