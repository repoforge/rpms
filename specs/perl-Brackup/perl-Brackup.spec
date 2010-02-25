# $Id$
# Authority: shuff
# Upstream: Brad Fitzpatrick <brad$danga,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Brackup

Summary: Flexible backup tool
Name: perl-Brackup
Version: 1.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Brackup/

Source: http://search.cpan.org/CPAN/authors/id/B/BR/BRADFITZ/Brackup-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Carp)
BuildRequires: perl(DBD::SQLite)
BuildRequires: perl(DBI)
BuildRequires: perl(Digest::SHA1)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::Temp)
BuildRequires: perl(File::stat)
BuildRequires: perl(IO::File)
BuildRequires: perl(MP3::Info)
BuildRequires: perl(Net::Amazon::S3)
BuildRequires: perl(Net::FTP)
BuildRequires: perl(Net::Mosso::CloudFiles)
BuildRequires: perl(Net::SFTP::Foreign)
BuildRequires: perl(POSIX)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Carp)
Requires: perl(DBD::SQLite)
Requires: perl(DBI)
Requires: perl(Digest::SHA1)
Requires: perl(Fcntl)
Requires: perl(File::Temp)
Requires: perl(File::stat)
Requires: perl(IO::File)
Requires: perl(MP3::Info)
Requires: perl(Net::Amazon::S3)
Requires: perl(Net::FTP)
Requires: perl(Net::Mosso::CloudFiles)
Requires: perl(Net::SFTP::Foreign)
Requires: perl(POSIX)

Provides: %{_bindir}/brackup
Provides: %{_bindir}/brackup-restore
Provides: %{_bindir}/brackup-target

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Slices, dices, encrypts, and sprays across the net.


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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man?/*
%{perl_vendorlib}/*
%{_bindir}/*

%changelog
* Thu Oct 29 2009 Steve Huff <shuff@vecna.org> - 1.09-1
- Initial package.
