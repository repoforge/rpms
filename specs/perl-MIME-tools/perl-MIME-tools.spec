# $Id$

# Authority: atrpms
%define rname MIME-tools

Summary: Perl modules for parsing (and creating!) MIME entities
Name: perl-MIME-tools
Version: 5.411
Release: 2
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MIME-tools/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cpan.org/authors/id/E/ER/ERYQ/%{rname}-%{version}a.tar.gz
Patch: http://www.roaringpenguin.com/mimedefang/mime-tools-patch.txt
Patch1: MIME-Tools.diff
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: perl(IO::Stringy) >= 1.211, perl-MailTools
Requires: perl(IO::Stringy) >= 1.211, perl-MailTools >= 1.15
%{?rh73:BuildRequires: perl(MIME::Base64) >= 2.04}
%{?rhel21:BuildRequires: perl-MIME-Base64 >= 2.04}

%description
MIME-tools - modules for parsing (and creating!) MIME entities Modules in this
toolkit : Abstract message holder (file, scalar, etc.), OO interface for
decoding MIME messages, an extracted and decoded MIME entity, Mail::Field
subclasses for parsing fields, a parsed MIME header (Mail::Header subclass),
parser and tool for building your own MIME parser, and utilities.

%prep
%setup -n %{rname}-%{version}
%patch -p1
%patch1 -p1

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}
#{__make} test

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALLING MANIFEST README* docs/ examples/
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
