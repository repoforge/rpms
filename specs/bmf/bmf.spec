# $Id$
# Authority: dag

Summary: Bayesian Mail Filter
Name: bmf
Version: 0.9.4
Release: 1%{?dist}
License: GPLv2
Group: Applications/Internet
URL: http://sourceforge.net/projects/bmf/

Source: http://dl.sf.net/bmf/bmf-%{version}.tar.gz
Patch1: bmf-0.9.4-optflags.patch
Patch2: bmf-0.9.4-disable_root_check.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: db4-devel
#BuildRequires: mysqlclient10-devel
BuildRequires: pkgconfig

%description
bmf is a self contained and extremely efficient Bayesian mail filter. See Paul
Graham's article "A Plan for Spam" for background information. It aims to be
faster, smaller, and more versatile than similar applications.

%prep
%setup
%patch1
%patch2

%build
./configure \
    --debug="no" \
    --with-libdb="%{_prefix}"
#    --with-mysql="test"

%{__make} %{?_smp_mflags} all CC="%{__cc}" OPTFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog LICENSE README TODO
%doc %{_mandir}/man1/bmf.1*
%doc %{_mandir}/man1/bmfconv.1*
%{_bindir}/bmf
%{_bindir}/bmfconv

%changelog
* Tue Oct 05 2010 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Initial package. (using DAR)
