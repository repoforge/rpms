# $Id$
# Authority: dag
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-Mail

Summary: Perl module to convert between DateTime and RFC2822/822 formats
Name: perl-DateTime-Format-Mail
Version: 0.30
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-Mail/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Format-Mail-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker), perl(Module::Build)
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
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Artistic AUTHORS Changes COPYING CREDITS LICENCE MANIFEST META.yml README notes/
%doc %{_mandir}/man3/DateTime::Format::Mail.3pm*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Format/
%{perl_vendorlib}/DateTime/Format/Mail.pm

%changelog
* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.30-1
- Initial package. (using DAR)
