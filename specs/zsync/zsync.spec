# $Id
# Authority: dag

Summary: Partial/differential file transfer client over HTTP
Name: zsync
Version: 0.3.3
Release: 1
License: Artistic
Group: Applications/Internet
URL: http://zsync.moria.org.uk/

Source: http://dl.sf.net/zsync/zsync-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
zsync is a file transfer program. It allows you to download a file from
a remote server, where you have a copy of an older version of the file
on your computer already. zsync downloads only the new parts of the file.

zsync uses the same algorithm as rsync. However, where rsync is designed
for synchronising data from one computer to another within an organisation,
zsync is designed for file distribution, with one file on a server to be
distributed to thousands of downloaders. zsync requires no special server
software just a web server to host the files and imposes no extra load on
the server, making it ideal for large scale file distribution.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr (-, root, root, 0755)
%doc COPYING INSTALL README
%doc %{_mandir}/man1/zsync.1*
%doc %{_mandir}/man1/zsyncmake.1*
%{_bindir}/zsync
%{_bindir}/zsyncmake
%exclude %{_docdir}/zsync/

%changelog
* Tue Apr 05 2005 Dag Wieers <dag@wieers.com> - 0.3.3-1
- Initial package. (using DAR)
