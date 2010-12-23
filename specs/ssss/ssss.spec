# $Id$
# Authority: shuff
# Upstream: B. Poettering <ssss$point-at-infinity,org>

Summary: Shamir's Secret Sharing Scheme
Name: ssss
Version: 0.5
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://point-at-infinity.org/ssss/

Source: http://point-at-infinity.org/ssss/ssss-%{version}.tar.gz
Source1: http://point-at-infinity.org/ssss/ssss.1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: gmp-devel
BuildRequires: make
BuildRequires: rpm-macros-rpmforge

%description
ssss is an implementation of Shamir's secret sharing scheme for UNIX/linux
machines. It is free software, the code is licensed under the GNU GPL. ssss
does both: the generation of shares for a known secret and the reconstruction
of a secret using user provided shares.

In cryptography, a secret sharing scheme is a method for distributing a secret
amongst a group of participants, each of which is allocated a share of the
secret. The secret can only be reconstructed when the shares are combined
together; individual shares are of no use on their own.

More formally, in a secret sharing scheme there is one dealer and n players.
The dealer gives a secret to the players, but only when specific conditions are
fulfilled. The dealer accomplishes this by giving each player a share in such a
way that any group of t (for threshold) or more players can together
reconstruct the secret but no group of less than t players can. Such a system
is called a (t,n)-threshold scheme.

%prep
%setup
%{__cp} %{_sourcedir}/ssss.1 .

%build
%{__make} %{?_smp_mflags} ssss-split

%install
%{__rm} -rf %{buildroot}

# install the binary
%{__install} -m755 -d %{buildroot}%{_bindir}
%{__install} -m755 ssss-split %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -f ssss-split ssss-combine
popd

# install the manpage
%{__install} -m755 -d %{buildroot}%{_mandir}/man1
%{__install} -m644 ssss.1 %{buildroot}%{_mandir}/man1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc.html HISTORY LICENSE THANKS
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Thu Dec 23 2010 Steve Huff <shuff@vecna.org> - 0.5-1
- Initial package.

