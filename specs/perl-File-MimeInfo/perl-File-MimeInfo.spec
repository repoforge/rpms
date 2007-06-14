# $Id$
# Authority: dag
# Upstream: Jaap Karssenberg <pardus$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-MimeInfo

Summary: Perl module to determine file type
Name: perl-File-MimeInfo
Version: 0.13
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-MimeInfo/

Source: http://www.cpan.org/modules/by-module/File/File-MimeInfo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)
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
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README t/magic/application_x-perl.txt
%doc %{_mandir}/man3/*.3pm*
%doc %{_mandir}/man1/mime*.1*
%{_bindir}/mimeopen
%{_bindir}/mimetype
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/MimeInfo/
%{perl_vendorlib}/File/MimeInfo.pm

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.13-1
- Initial package. (using DAR)
