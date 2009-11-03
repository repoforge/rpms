# $Id$
# Authority: dag
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Folder

Summary: Perl module to read all the messages from a folder as Email::Simple objects
Name: perl-Email-Folder
Version: 0.855
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Folder/

Source: http://www.cpan.org/modules/by-module/Email/Email-Folder-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# From yaml build_requires
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
BuildRequires: perl(Email::FolderType) >= 0.6
BuildRequires: perl(Email::Simple)
BuildRequires: perl(Test::More) >= 0.47


%description
perl-Email-Folder is a Perl module to read all the messages from
a folder as Email::Simple objects.

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
%doc Changes LICENSE MANIFEST META.yml README TODO
%doc %{_mandir}/man3/Email::Folder.3pm*
%doc %{_mandir}/man3/Email::Folder::MH.3pm*
%doc %{_mandir}/man3/Email::Folder::Maildir.3pm*
%doc %{_mandir}/man3/Email::Folder::Mbox.3pm*
%doc %{_mandir}/man3/Email::Folder::Reader.3pm*
%dir %{perl_vendorlib}/Email/
%{perl_vendorlib}/Email/Folder/
%{perl_vendorlib}/Email/Folder.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.855-1
- Updated to version 0.855.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.854-1
- Updated to release 0.854.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.853-1
- Initial package. (using DAR)
