# $Id$
# Authority: dag
# Upstream: Dave Rolsky <autarch$urth,org>

### EL6 ships with perl-DateTime-Format-DateParse-0.04-1.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-Mail
%define real_version 0.30.1

Summary: Perl module to convert between DateTime and RFC2822/822 formats
Name: perl-DateTime-Format-Mail
Version: 0.3001
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-Mail/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Format-Mail-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build)
Requires: perl

%description
DateTime-Format-Mail is a Perl module to convert between DateTime
and RFC2822/822 formats.

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
%doc AUTHORS Artistic COPYING CREDITS Changes LICENCE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/DateTime::Format::Mail.3pm*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Format/
#%{perl_vendorlib}/DateTime/Format/Mail/
%{perl_vendorlib}/DateTime/Format/Mail.pm

%changelog
* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.3001-1
- Switch to upstream version.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.30.1-1
- Updated to release 0.3001.

* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.30-1
- Initial package. (using DAR)
