# $Id$

# Authority: dag

Summary: Use the Razor catalog server to filter spam messages.
Name: razor-agents
Version: 1.20
Release: 1
Group: Applications/Internet
License: Artistic
URL: http://razor.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/razor-agents/razor-agents-%{version}.tar.gz
Patch0: %{name}-makefile.patch
Patch1: %{name}-redhat.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: perl, perl(Net::DNS), perl(Digest::SHA1), perl(Time::HiRes), perl(MIME::Base64)
BuildRequires: perl(Mail::Header), perl(Mail::Internet)
#BuildRequires: perl-MailTools
BuildRequires: perl(Getopt::Long), perl(Net::Ping)
Requires: perl-Razor = %{version}-%{release}
Prereq: /sbin/chkconfig

%description
Vipul's Razor is a distributed, collaborative, spam detection and filtering
network.  Razor establishes a distributed and constantly updating catalogue of
spam in propagation.  This catalogue is used by clients to filter out known 
spam.  On receiving a spam, a Razor Reporting Agent (run by an end-user or a 
troll box) calculates and submits a 20-character unique identification of the
spam (a SHA Digest) to its closest Razor Catalogue Server.  The Catalogue 
Server echos this signature to other trusted servers after storing it in its
database.  Prior to manual processing or transport-level reception, Razor 
Filtering Agents (end-users and MTAs) check their incoming mail against a 
Catalogue Server and filter out or deny transport in case of a signature 
match.  Catalogued spam, once identified and reported by a Reporting Agent, 
can be blocked out by the rest of the Filtering Agents on the network. 

%package -n perl-Razor
Group: Applications/CPAN
Summary: perl-Razor Perl module
Obsoletes: razor-agents-sdk

%description -n perl-Razor
Implements perl class Razor, a SPAM/UCE filtering agent.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
CFLAGS="%{optflags}" perl Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLMAN5DIR="%{buildroot}%{_mandir}/man5" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"
%{__mv} -f Changes Changes.pod
pod2text Changes.pod > Changes

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/mail/razor/
%{__install} -m0644 etc/razor.conf %{buildroot}%{_sysconfdir}/mail/razor/
%{__install} -m0664 etc/whitelist %{buildroot}%{_sysconfdir}/mail/razor/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/*
%{_bindir}/*

%files -n perl-Razor
%defattr(-, root, root, 0755)
%doc ARTISTIC Changes sample.txt
%doc %{_mandir}/man3/*
%config(noreplace) %{_sysconfdir}/mail/razor/
%{_libdir}/perl5/

%changelog
* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 1.20-0
- Initial package. (using DAR)
