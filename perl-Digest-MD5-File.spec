#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Digest
%define	pnam	MD5-File
Summary:	Digest::MD5::File - getting MD5 sums for files and URLs
Summary(pl.UTF-8):   Digest::MD5::File - uzyskiwanie sum MD5 dla plikĂłw i URL-i
Name:		perl-Digest-MD5-File
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	385c5ff7dadd240f6a2194a67f8f9b47
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Get MD5 sums for files of a given path or content of a given URL.

%description -l pl.UTF-8
Ten moduĹ pozwala uzyskaÄ sumy MD5 dla plikĂłw o podanej ĹcieĹźce lub
dla zawartoĹci podanego URL-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Digest/MD5/*.pm
%{_mandir}/man3/*
