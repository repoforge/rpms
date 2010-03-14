# $Id$
# Authority: shuff
# Upstream: Bill Yerazunis <wsy$users,sourceforge,net>

# update this with every release
%define codename BlameMichelson

Summary: Controllable Regex Mutilator
Name: crm114
Version: 20100106
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://crm114.sourceforge.net/

Source: http://crm114.sourceforge.net/tarballs/crm114-%{version}-%{codename}.src.tar.gz
Patch0: %{name}_Makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc, make
BuildRequires: glibc-devel
BuildRequires: tre-devel >= 0.7.5

%description
CRM114 is a system to examine incoming e-mail, system log streams, data files
or other data streams, and to sort, filter, or alter the incoming files or data
streams according to the user's wildest desires. Criteria for categorization of
data can be via a host of methods, including regexes, approximate regexes, a
Hidden Markov Model, Bayesian Chain Rule, Orthogonal Sparse Bigrams, Winnow,
Correlation, KNN/Hyperspace, Bit Entropy, CLUMP, SVM, Neural Networks (or by
other means- it's all programmable).

Spam is the big target with CRM114, but it's not a specialized Email-only tool.
CRM114 has been used to sort web pages, resumes, blog entries, log files, and
lots of other things. Accuracy can be as high as 99.9%. In other words, CRM114
learns, and it learns fast.

CRM114 is compatible with SpamAssassin or other spam-flagging software; it can
also be pipelined in front of or behind procmail. CRM114 is also useful as a
syslog or firewall log filter, to alert you to important events but ignore the
ones that aren't meaningful. 

%package emacs
Summary: Emacs mode for CRM114
Group: Applications/Text
Requires: %{name} = %{version}
Requires: emacs-common

%description emacs
Emacs mode for editing CRM114 config files.

%prep
%setup -n %{name}-%{version}-%{codename}.src
%patch0 -p1

%build
%{__make} FLAGS="%{optflags}" LDFLAGS="-L%{_libdir}"

%install
%{__rm} -rf %{buildroot}
%{__install} -m0755 -d %{buildroot}%{_bindir}
%{__install} -m0755 -d %{buildroot}%{_datadir}/emacs/site-lisp/
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc *.txt *.recipe *.example *.cf
%{_bindir}/*

%files emacs
%dir %{_datadir}/emacs/site-lisp/
%{_datadir}/emacs/site-lisp/*

%changelog
* Sat Mar 13 2010 Steve Huff <shuff@vecna.org> - 20100106-1
- Initial package.
